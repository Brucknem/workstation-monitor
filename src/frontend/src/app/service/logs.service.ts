import { Injectable } from '@angular/core';
import { MOCK_LOG } from './mock-logs';
import { Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class LogsService {
  private columns = Object.keys(MOCK_LOG);

  constructor() {
    delete this.columns['timestamp'];
  }

  getLogs(): Observable<any> {
    return of(MOCK_LOG);
  }

  getColumns(): Observable<string[]> {
    return of(this.columns);
  }

  getIndices(): Observable<string[]> {
    return of(this.columns);
  }
}
