import { Component, Input, OnInit, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-selection-list',
  templateUrl: './selection-list.component.html',
  styleUrls: ['./selection-list.component.css'],
})
export class SelectionListComponent implements OnInit {
  @Input()
  selectedOption: string;

  @Input()
  values: string[];

  @Output()
  selectValueColumns = new EventEmitter<string>();

  constructor() {}

  ngOnInit(): void {}

  onSelectDevices($event: any): void {
    this.selectValueColumns.emit(this.selectedOption);
  }
}
