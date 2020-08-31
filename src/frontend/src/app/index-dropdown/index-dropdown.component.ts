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

  @Output()
  selectionChanged = new EventEmitter<{ key: string; value: string }>();

  constructor() {}

  ngOnInit(): void {}

  onNgModelChange($event: any): void {
    const indices = {};
    const values = $event.value;
    for (const value of values) {
      const split = value.split(';');
      if (!(split[0] in indices)) {
        indices[split[0]] = [];
      }
      indices[split[0]].push(split[1]);
    }
    this.selectionChanged.emit({ key: indices[0], value: indices[1] });
  }
}
