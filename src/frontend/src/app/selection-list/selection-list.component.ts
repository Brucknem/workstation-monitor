import { Component, Input, OnInit, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-selection-list',
  templateUrl: './selection-list.component.html',
  styleUrls: ['./selection-list.component.css'],
})
export class SelectionListComponent implements OnInit {
  selectedOptions: string[];

  @Input()
  values: string[];

  @Input()
  selectedDeviceType: string;

  @Input()
  selectedDevices: string[];

  @Output()
  selectValueColumns = new EventEmitter<string[]>();

  constructor() {}

  ngOnInit(): void {}

  onSelectDevices($event: any): void {
    this.selectValueColumns.emit(this.selectedOptions);
  }
}
