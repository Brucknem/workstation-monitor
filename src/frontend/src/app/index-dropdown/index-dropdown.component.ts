import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { LogsService } from '../service/logs.service';

@Component({
  selector: 'app-index-dropdown',
  templateUrl: './index-dropdown.component.html',
  styleUrls: ['./index-dropdown.component.css'],
})
export class IndexDropdownComponent implements OnInit {
  selectedDeviceType;

  @Input()
  values: { [p: string]: any[] };

  @Output()
  deviceTypeSelectionChanged = new EventEmitter<string>();

  @Output()
  deviceSelectionChanged = new EventEmitter<string[]>();

  constructor() {}

  ngOnInit(): void {}

  onSelectDeviceType($event: any): void {
    this.deviceTypeSelectionChanged.emit($event.value);
  }

  onSelectDevice($event: any): void {
    const indices = {};
    const values = $event.value;
    for (const value of values) {
      const split = value.split(';');
      if (!(split[0] in indices)) {
        indices[split[0]] = [];
      }
      indices[split[0]].push(split[1]);
    }
    this.deviceSelectionChanged.emit([]);
  }
}
