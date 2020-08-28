import { Component, OnInit } from '@angular/core';
import { LogsService } from '../service/logs.service';
import { FormControl } from '@angular/forms';

@Component({
  selector: 'app-index-selector',
  templateUrl: './index-selector.component.html',
  styleUrls: ['./index-selector.component.css'],
})
export class IndexSelectorComponent implements OnInit {
  log: object;
  columns: string[];
  indices: string[];
  selectedIndices = new FormControl();
  selectedColumns = new FormControl();

  favoriteSeason = new FormControl();
  seasons: string[] = ['Winter', 'Spring', 'Summer', 'Autumn'];

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
}
