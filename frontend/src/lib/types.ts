export type QuestionStatus = 'unsolved' | 'solved' | 'review' | 'failed';

export interface SocraticClues {
  title: string;
  level1: string;
  level2: string;
  level3: string;
  level4: string;
}

export interface Question {
  id: string;
  exam_id: string;
  tag: string;
  area: string;
  subtopic: string;
  question_type: string;
  page: number;
  has_image: boolean;
  text: string;
  flag?: string | null;
  errata?: string | null;
  image: string;
  clues: SocraticClues;
  twin_id?: string | null;
  twin_stem?: string | null;
}

export interface ExamInfo {
  id: string;
  year: number;
  semester: number;
  filename?: string;
  num_pages?: number;
  exam_type?: string;
  total_questions: number;
}

export interface SubtopicInfo {
  name: string;
  count: number;
}

export interface AreaConceptTree {
  total: number;
  subtopics: SubtopicInfo[];
}

export interface TwinPair {
  exam_id: string;
  stem: string;
  area: string;
  subtopic: string;
  qid_a: string;
  qid_b: string;
  text_a: string;
  text_b: string;
  diff: string;
  image_a: string;
  image_b: string;
}

export interface BankData {
  version: string;
  generated_at?: string | null;
  stats: {
    total_questions: number;
    total_pairs: number;
    total_exams: number;
    areas_count: number;
  };
  exams: ExamInfo[];
  concept_tree: Record<string, AreaConceptTree>;
  pairs: TwinPair[];
  questions: Question[];
}

export interface QuestionUserState {
  status: QuestionStatus;
  notes?: string;
  time_spent_seconds?: number;
  last_updated?: string;
}

export interface UserProfile {
  name: string;
  created_at: string;
  questions: Record<string, QuestionUserState>;
}
