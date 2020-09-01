import { Injectable } from '@angular/core';
import { MOCK_LOG } from './mock-logs';
import { Observable, of } from 'rxjs';
import { group } from '@angular/animations';
import { timestamp } from 'rxjs/operators';

@Injectable({
  providedIn: 'root',
})
export class LogsService {
  private columns = Object.keys(MOCK_LOG);
  private readonly uniqueColumns;
  private indices: { [column: string]: any[] } = {};

  constructor() {
    const timestampIndex = this.columns.indexOf('timestamp', 0);
    if (timestampIndex > -1) {
      this.columns.splice(timestampIndex, 1);
    }
    this.uniqueColumns = this.calculateUniqueColumns();
    this.calculateIndices();
  }

  getRawLog(): object {
    return MOCK_LOG;
  }

  /**
   * Calculates all groups of indices within the given column
   * @param column The name of the column to group by
   * @param filter
   */
  groupBy(column: string, filter: string[] = null): { [p: string]: number[] } {
    const values = this.getRawLog()[column];
    const groups = {};
    for (const key in values) {
      const value = values[key];
      if (filter && filter.indexOf(value) < 0) {
        continue;
      }
      if (!(value in groups)) {
        groups[value] = [];
      }
      groups[value].push(key);
    }
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
    if (!this.uniqueColumns) {
      return;
    }
    for (const column of this.uniqueColumns) {
      const uniqueElements = this.getRawLog()[column];
      this.indices[column] = [];
      for (const uniqueElement of Object.values(uniqueElements)) {
        if (this.indices[column].indexOf(uniqueElement) < 0) {
          this.indices[column].push(uniqueElement);
        }
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
    // if (groups.length[0] === this.columns.length) {
    //   return [];
    // }

    for (const column of this.columns) {
      const values = this.getRawLog()[column];
      let indices = null;
      let validIndex = true;
      for (const name in groups) {
        const group = groups[name];
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

  getIndices(): Observable<{ [column: string]: any[] }> {
    return of(this.indices);
  }

  getValues(deviceType: string, devices: string[], valueColumn: string[]) {
    const values = [];
    // if (devices.length === 0 || valueColumn === '') {
    //   return values;
    // }
    //
    // const groups = this.groupBy(deviceType, devices);
    // for (const groupName in groups) {
    //   const currentValues = { name: groupName, series: [] };
    //   const timestamps = this.getRawLog()['timestamp'];
    //   const series = this.getRawLog()[valueColumn];
    //   const indices = groups[groupName];
    //   for (const index of indices) {
    //     const name = new Date(timestamps[index]);
    //     const value = series[index];
    //     currentValues['series'].push({
    //       name,
    //       value,
    //     });
    //   }
    //   values.push(currentValues);
    // }

    return values;
  }
}
