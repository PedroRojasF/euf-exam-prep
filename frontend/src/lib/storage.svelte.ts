import type { QuestionStatus, QuestionUserState, UserProfile } from './types';

const ACTIVE_PROFILE_KEY = 'euf_active_profile';
const PROFILE_PREFIX = 'euf_profile_';
const PROFILES_LIST_KEY = 'euf_profiles_index';

export class ProfileStore {
  activeProfileName = $state<string>('candidato_padrao');
  profilesList = $state<string[]>(['candidato_padrao']);
  currentProfileData = $state<UserProfile>({
    name: 'candidato_padrao',
    created_at: new Date().toISOString(),
    questions: {}
  });

  constructor() {
    if (typeof window !== 'undefined') {
      this.init();
    }
  }

  private init() {
    try {
      const storedList = localStorage.getItem(PROFILES_LIST_KEY);
      if (storedList) {
        this.profilesList = JSON.parse(storedList);
      } else {
        this.profilesList = ['candidato_padrao'];
        localStorage.setItem(PROFILES_LIST_KEY, JSON.stringify(this.profilesList));
      }

      const active = localStorage.getItem(ACTIVE_PROFILE_KEY);
      if (active && this.profilesList.includes(active)) {
        this.activeProfileName = active;
      } else {
        this.activeProfileName = this.profilesList[0] || 'candidato_padrao';
      }

      this.loadActiveProfile();
    } catch (e) {
      console.error('Error initializing ProfileStore from localStorage', e);
    }
  }

  loadActiveProfile() {
    try {
      const raw = localStorage.getItem(`${PROFILE_PREFIX}${this.activeProfileName}`);
      if (raw) {
        this.currentProfileData = JSON.parse(raw);
      } else {
        this.currentProfileData = {
          name: this.activeProfileName,
          created_at: new Date().toISOString(),
          questions: {}
        };
        this.persistCurrentProfile();
      }
    } catch (e) {
      console.error('Error loading profile', e);
    }
  }

  switchProfile(name: string) {
    if (!this.profilesList.includes(name)) {
      this.profilesList = [...this.profilesList, name];
      localStorage.setItem(PROFILES_LIST_KEY, JSON.stringify(this.profilesList));
    }
    this.activeProfileName = name;
    localStorage.setItem(ACTIVE_PROFILE_KEY, name);
    this.loadActiveProfile();
  }

  createProfile(name: string) {
    const cleanName = name.trim();
    if (!cleanName) return;
    if (!this.profilesList.includes(cleanName)) {
      this.profilesList = [...this.profilesList, cleanName];
      localStorage.setItem(PROFILES_LIST_KEY, JSON.stringify(this.profilesList));
    }
    this.switchProfile(cleanName);
  }

  deleteProfile(name: string) {
    if (this.profilesList.length <= 1) {
      alert('Não é possível excluir o único perfil existente.');
      return;
    }
    this.profilesList = this.profilesList.filter(p => p !== name);
    localStorage.setItem(PROFILES_LIST_KEY, JSON.stringify(this.profilesList));
    localStorage.removeItem(`${PROFILE_PREFIX}${name}`);

    if (this.activeProfileName === name) {
      this.switchProfile(this.profilesList[0]);
    }
  }

  getQuestionState(qid: string): QuestionUserState {
    return this.currentProfileData.questions[qid] || {
      status: 'unsolved',
      notes: ''
    };
  }

  updateQuestionStatus(qid: string, status: QuestionStatus) {
    const current = this.getQuestionState(qid);
    this.currentProfileData.questions[qid] = {
      ...current,
      status,
      last_updated: new Date().toISOString()
    };
    this.persistCurrentProfile();
  }

  updateQuestionNotes(qid: string, notes: string) {
    const current = this.getQuestionState(qid);
    this.currentProfileData.questions[qid] = {
      ...current,
      notes,
      last_updated: new Date().toISOString()
    };
    this.persistCurrentProfile();
  }

  addTimeSpent(qid: string, seconds: number) {
    const current = this.getQuestionState(qid);
    const prev = current.time_spent_seconds || 0;
    this.currentProfileData.questions[qid] = {
      ...current,
      time_spent_seconds: prev + seconds,
      last_updated: new Date().toISOString()
    };
    this.persistCurrentProfile();
  }

  private persistCurrentProfile() {
    try {
      localStorage.setItem(
        `${PROFILE_PREFIX}${this.activeProfileName}`,
        JSON.stringify(this.currentProfileData)
      );
    } catch (e) {
      console.error('Error saving profile to localStorage', e);
    }
  }

  exportProfileAsJSON(): string {
    return JSON.stringify(this.currentProfileData, null, 2);
  }

  importProfileFromJSON(jsonString: string) {
    try {
      const data = JSON.parse(jsonString) as UserProfile;
      if (!data.name || typeof data.questions !== 'object') {
        throw new Error('Formato de perfil inválido.');
      }
      this.createProfile(data.name);
      this.currentProfileData = data;
      this.persistCurrentProfile();
      return true;
    } catch (e) {
      console.error('Error importing profile JSON', e);
      throw e;
    }
  }
}

export const profileStore = new ProfileStore();
