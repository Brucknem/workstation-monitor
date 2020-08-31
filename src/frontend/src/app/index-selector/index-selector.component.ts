import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { LogsService } from '../service/logs.service';
import { FormControl } from '@angular/forms';
import { MatSelectionListChange } from '@angular/material/list';

@Component({
  selector: 'app-index-selector',
  templateUrl: './index-selector.component.html',
  styleUrls: ['./index-selector.component.css'],
})
export class IndexSelectorComponent implements OnInit {
  log: object;
  columns: string[];
  valueColumns: string[];
  indices: { [p: string]: any[] };
  selectedDevice: string;

  constructor(private logService: LogsService) {}

  ngOnInit(): void {
    this.getLogs();
    this.getColumns();
    this.getIndices();
  }

  getLogs(): void {
    this.logService.getLogs().subscribe((log) => (this.log = log));
  }

  getColumns(): void {
    this.logService
      .getColumns()
      .subscribe((columns) => (this.columns = columns));
  }

  getIndices(): void {
    this.logService
      .getIndices()
      .subscribe((indices) => (this.indices = indices));
  }

  onSelectDeviceType($event: string): void {
    this.selectedDevice = $event;
    console.log(this.selectedDevice);
    this.valueColumns = Object.assign([], this.columns);
    const index = this.valueColumns.indexOf(this.selectedDevice, 0);
    if (index > -1) {
      this.valueColumns.splice(index, 1);
    }
  }

  selectIndices($event: any): void {
    console.log($event);
    // this.logService.selectIndices($event);
  }

  selectColumns($event: string[]): void {
    this.logService.selectColumns($event);
  }
}
