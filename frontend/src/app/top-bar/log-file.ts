interface IDictionary {
  [index: string]: any;
}

export interface LogFile {
  data: IDictionary;
  indices: string[];
}
