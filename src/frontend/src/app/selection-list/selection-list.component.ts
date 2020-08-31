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

  @Output()
  selectionChanged = new EventEmitter<string[]>();

  constructor() {}

  ngOnInit(): void {}

  onNgModelChange($event: any): void {
    this.selectionChanged.emit($event);
  }
}
