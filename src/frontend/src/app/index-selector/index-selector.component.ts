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
  indices: string[];

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

  selectIndices($event: string[]): void {
    this.logService.selectIndices($event);
  }

  selectColumns($event: string[]): void {
    this.logService.selectColumns($event);
  }
}
