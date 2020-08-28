import { Injectable } from '@angular/core';
import { MOCK_LOG } from './mock-logs';
import { Observable, of } from 'rxjs';
import { group } from '@angular/animations';

@Injectable({
  providedIn: 'root',
})
export class LogsService {
  private columns = Object.keys(MOCK_LOG);
  private indices: string[];
  private selectedIndices: string[];
  private selectedColumns: string[];

  constructor() {
    const timestampIndex = this.columns.indexOf('timestamp', 0);
    if (timestampIndex > -1) {
      this.columns.splice(timestampIndex, 1);
    }
    this.calculateIndices();
  }

  getRawLog(): object {
    return MOCK_LOG;
  }

  /**
   * Calculates all groups of indices within the given column
   * @param column The name of the column to group by
   */
  groupBy(column: string): any[][] {
    const value = this.getRawLog()[column];
    let currentValue = -1;
    const groups = [];
    let currentGroup = [];
    for (const i in value) {
      const timestamp = value[i];
      if (timestamp !== currentValue) {
        currentValue = timestamp;
        groups.push(currentGroup);
        currentGroup = [i];
        continue;
      }
      currentGroup.push(i);
    }
    groups.splice(0, 1);
    groups.push(currentGroup);
    return groups;
  }

  arraysEqual(first: any[], second: any[]): boolean {
    for (const f of first) {
      if (second.indexOf(f) < 0) {
        return false;
      }
    }
    return true;
  }

  calculateIndices(): void {
    const uniqueColumns = this.calculateUniqueColumns();
    console.log(uniqueColumns);
    if (!uniqueColumns) {
      return;
    }
    this.indices = [];
    for (const column of uniqueColumns) {
      console.log(column);
      const uniqueElements = this.getRawLog()[column];
      console.log(uniqueElements);
      for (const uniqueElement of uniqueElements) {
        this.indices.push(uniqueElement);
      }
    }
  }

  /**
   * Calculates all columns that can be used to clearly identify hardware.
   * A column is unique if for every group of values per timestamp are unique.
   */
  calculateUniqueColumns(): string[] {
    const groups = this.groupBy('timestamp');
    const uniqueColumns = [];
    if (groups.length === this.columns.length) {
      return [];
    }

    for (const column of this.columns) {
      const values = this.getRawLog()[column];
      let indices = null;
      let validIndex = true;
      for (const group of groups) {
        const groupValues = [];
        for (const index of group) {
          groupValues.push(values[index]);
        }
        if (new Set(groupValues).size !== groupValues.length) {
          validIndex = false;
          break;
        }
        if (indices === null) {
          indices = groupValues;
        }

        if (!this.arraysEqual(groupValues, indices)) {
          validIndex = false;
          break;
        }
      }
      if (validIndex) {
        uniqueColumns.push(column);
      }
    }
    return uniqueColumns;
  }

  getLogs(): Observable<any> {
    return of(this.getRawLog());
  }

  getColumns(): Observable<string[]> {
    return of(this.columns);
  }

  getIndices(): Observable<string[]> {
    return of(this.indices);
  }

  selectIndices(indices: string[]): void {
    this.selectedIndices = indices;
  }
  selectColumns(columns: string[]): void {
    this.selectedColumns = columns;
  }
}
