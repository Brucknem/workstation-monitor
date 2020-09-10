import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { LogsService } from '../../../../service/logs.service';

@Component({
  selector: 'app-select-log-file',
  templateUrl: './select-log-file.component.html',
  styleUrls: ['./select-log-file.component.css'],
})
export class SelectLogFileComponent implements OnInit {
  @Output()
  selectLogFile = new EventEmitter<string>();

  constructor(public logsService: LogsService) {}

  ngOnInit(): void {}
}
