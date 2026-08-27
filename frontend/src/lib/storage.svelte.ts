import type { QuestionStatus, QuestionUserState, UserProfile } from './types';
import { type Language, DICTIONARY, type Translations } from './i18n';

const ACTIVE_PROFILE_KEY = 'euf_active_profile';
const PROFILE_PREFIX = 'euf_profile_';
const PROFILES_LIST_KEY = 'euf_profiles_index';
const THEME_KEY = 'euf_app_theme';
const LANG_KEY = 'euf_app_lang';

export class AppStore {
  activeProfileName = $state<string>('candidato_padrao');
  profilesList = $state<string[]>(['candidato_padrao']);
  currentProfileData = $state<UserProfile>({
    name: 'candidato_padrao',
    created_at: new Date().toISOString(),
    questions: {}
  });

  // Theme & Language State
  theme = $state<'light' | 'dark'>('light');
  lang = $state<Language>('pt');

  constructor() {
    if (typeof window !== 'undefined') {
      this.init();
    }
  }

  private init() {
    try {
      // 1. Init Theme
      const savedTheme = localStorage.getItem(THEME_KEY) as 'light' | 'dark' | null;
      if (savedTheme === 'dark' || savedTheme === 'light') {
        this.theme = savedTheme;
      } else {
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        this.theme = prefersDark ? 'dark' : 'light';
      }
      this.applyThemeClass();

      // 2. Init Language
      const savedLang = localStorage.getItem(LANG_KEY) as Language | null;
      if (savedLang && ['pt', 'es', 'en'].includes(savedLang)) {
        this.lang = savedLang;
      } else {
        const browserLang = navigator.language.slice(0, 2);
        if (browserLang === 'es') this.lang = 'es';
        else if (browserLang === 'en') this.lang = 'en';
        else this.lang = 'pt';
      }

      // 3. Init Profiles
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
      console.error('Error initializing AppStore from localStorage', e);
    }
  }

  toggleTheme() {
    this.theme = this.theme === 'light' ? 'dark' : 'light';
    localStorage.setItem(THEME_KEY, this.theme);
    this.applyThemeClass();
  }

  setTheme(t: 'light' | 'dark') {
    this.theme = t;
    localStorage.setItem(THEME_KEY, t);
    this.applyThemeClass();
  }

  private applyThemeClass() {
    if (typeof document !== 'undefined') {
      if (this.theme === 'dark') {
        document.documentElement.classList.add('dark');
      } else {
        document.documentElement.classList.remove('dark');
      }
    }
  }

  setLanguage(l: Language) {
    this.lang = l;
    localStorage.setItem(LANG_KEY, l);
  }

  t(key: keyof Translations): string {
    const dict = DICTIONARY[this.lang] || DICTIONARY.pt;
    return dict[key] || DICTIONARY.pt[key] || key;
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
      alert('Não é possível excluir o único perfil.');
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

export const profileStore = new AppStore();
