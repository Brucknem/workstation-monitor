import {
  ChangeDetectionStrategy,
  Component,
  EventEmitter,
  Input,
  OnInit,
  Output,
} from '@angular/core';
import { Index } from '../../../../service/logs.service';

@Component({
  selector: 'app-select-index',
  templateUrl: './select-index.component.html',
  styleUrls: ['./select-index.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class SelectIndexComponent implements OnInit {
  @Input()
  indices?: Index;

  @Output()
  deviceTypeSelectionChanged = new EventEmitter<string>();

  @Output()
  devicesSelectionChanged = new EventEmitter<string[]>();

  ngOnInit(): void {}
}
