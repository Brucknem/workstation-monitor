import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { LogsService } from '../service/logs.service';

@Component({
  selector: 'app-index-dropdown',
  templateUrl: './index-dropdown.component.html',
  styleUrls: ['./index-dropdown.component.css'],
})
export class IndexDropdownComponent implements OnInit {
  @Input()
  values: { [p: string]: any[] };

  @Input()
  selectedValueColumns: string[];

  @Output()
  deviceTypeSelectionChanged = new EventEmitter<string>();

  @Output()
  devicesSelectionChanged = new EventEmitter<string[]>();

  selectedDeviceType;
  selectedDevices;

  ngOnInit(): void {}
}
