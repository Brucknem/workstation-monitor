import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-index-dropdown',
  templateUrl: './index-dropdown.component.html',
  styleUrls: ['./index-dropdown.component.css'],
})
export class IndexDropdownComponent implements OnInit {
  @Input()
  values: { [p: string]: any[] };

  @Output()
  deviceTypeSelectionChanged = new EventEmitter<string>();

  @Output()
  devicesSelectionChanged = new EventEmitter<string[]>();

  @Input()
  selectedDeviceType;

  @Input()
  selectedDevices;

  ngOnInit(): void {}
}
