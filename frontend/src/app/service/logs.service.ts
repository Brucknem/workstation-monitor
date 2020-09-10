import { Injectable } from '@angular/core';
import { MOCK_LOG } from './mock-logs';
import { Observable, of } from 'rxjs';

export class Index {
  [column: string]: any[];
}

@Injectable({
  providedIn: 'root',
})
export class LogsService {
  /**
   * The logs from which data can be displayed.
   * @private
   */
  private logs = MOCK_LOG;

  /**
   * The columns associated to the logs.
   * @see logs
   * @private
   */
  private columns: { [log: string]: string[] } = {};
  private uniqueColumns: { [log: string]: string[] } = {};
  private indices: { [log: string]: Index } = {};

  /**
   * @constructor
   */
  constructor() {
    for (const [name, log] of Object.entries(this.logs)) {
      this.columns[name] = LogsService.getColumns(log);
      this.uniqueColumns[name] = this.calculateUniqueColumns(
        log,
        this.columns[name]
      );
      this.indices[name] = this.calculateIndices(log, this.uniqueColumns[name]);

      // console.log(this.columns[name]);
      // console.log(this.uniqueColumns[name]);
      // console.log(this.indices[name]);
    }
  }

  /**
   * Extracts the columns of the given log and removes the timestamp column if present.
   * @param log The log to extract the columns from.
   * @private
   */
  private static getColumns(log: object): string[] {
    const columns = Object.keys(log);
    const timestampIndex = columns.indexOf('timestamp', 0);
    if (timestampIndex > -1) {
      columns.splice(timestampIndex, 1);
    }
    return columns;
  }

  getLogNames = () => of(Object.keys(this.logs).sort());
  getRawLog = (name: string = 'cpu') => this.logs[name];

  /**
   * Calculates all groups of indices within the given column in the given log.
   * @param log The log from which the columns are taken.
   * @param column The log after which to group.
   * @param filter Some values to ignore when calculating the groups.
   */
  groupBy(
    log: object,
    column: string,
    filter: any[] = null
  ): { [p: string]: any[] } {
    const groups = {};
    const values: { [p: string]: any } = log[column];
    for (const [key, value] of Object.entries(values)) {
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

  calculateIndices(log: any, uniqueColumns: string[]): Index {
    const indices = new Index();
    if (!this.uniqueColumns) {
      return;
    }
    for (const column of uniqueColumns) {
      const uniqueElements = log[column];
      indices[column] = [];
      for (const uniqueElement of Object.values(uniqueElements)) {
        if (indices[column].indexOf(uniqueElement) < 0) {
          indices[column].push(uniqueElement);
        }
      }
    }
    return indices;
  }

  /**
   * Calculates all columns that can be used to clearly identify hardware.
   * A column is unique if for every group of values per timestamp are unique.
   */
  calculateUniqueColumns(log: object, columns: string[]): string[] {
    const groups = this.groupBy(log, 'timestamp');
    const uniqueColumns = [];
    if (Object.values(groups).every((group) => group.length <= 1)) {
      return columns;
    }

    for (const column of columns) {
      const values = log[column];
      let indices = null;
      let validIndex = true;
      // tslint:disable-next-line:forin
      for (const name in groups) {
        if (!groups.hasOwnProperty(name)) {
          break;
        }
        const currentGroup = groups[name];
        const groupValues = [];
        for (const index of currentGroup) {
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
    return of();
    //    return of(this.getRawLog());
  }

  getColumns(logFileName: string): Observable<string[]> {
    return of(this.columns[logFileName].sort());
  }

  getIndices(logFileName: string): Observable<{ [column: string]: any[] }> {
    return of(this.indices[logFileName]);
  }

  getValues(
    deviceType: string,
    devices: string[],
    valueColumns: string[]
  ): any[] {
    // const values = [];
    // if (devices.length === 0 || valueColumns.length === 0) {
    //   return values;
    // }
    //
    // const groups = this.groupBy(deviceType, devices);
    // // @ts-ignore
    // const timestamps = this.getRawLog().timestamp;
    //
    // // tslint:disable-next-line:forin
    // for (const groupName in groups) {
    //   for (const column of valueColumns) {
    //     const series = this.getRawLog()[column];
    //     const legendLabel = `${groupName} [${column}]`;
    //     const currentValues = { name: legendLabel, series: [] };
    //     const indices = groups[groupName];
    //     for (const index of indices) {
    //       const name = new Date(timestamps[index]);
    //       const value = series[index];
    //       if (isNaN(value)) {
    //         console.log(value);
    //         continue;
    //       }
    //       currentValues.series.push({
    //         name,
    //         value,
    //       });
    //     }
    //     if (currentValues.series.length > 0) {
    //       values.push(currentValues);
    //     }
    //   }
    // }
    //
    // return values;

    return [];
  }

  deleteLog(name: string): void {
    delete this.logs[name];
  }

  addLog(name: string, content: any): void {
    this.logs[name] = { yeet: 'Yeet' };
  }
}
