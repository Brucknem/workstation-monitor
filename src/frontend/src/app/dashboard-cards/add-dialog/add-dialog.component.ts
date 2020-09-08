import { Component, Input, OnInit, EventEmitter } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { LogsService } from '../../service/logs.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-add-dialog',
  templateUrl: './add-dialog.component.html',
  styleUrls: ['./add-dialog.component.css'],
})
export class AddDialogComponent implements OnInit {
  @Input()
  selectedLog: string;

  availableLogs: Observable<string[]>;

  logSelectedEvent = new EventEmitter<string>();

  constructor(public logsService: LogsService) {}

  ngOnInit(): void {
    this.availableLogs = this.logsService.getLogNames();
  }
}
