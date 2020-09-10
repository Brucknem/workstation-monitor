import {
  ChangeDetectionStrategy,
  Component,
  Input,
  OnInit,
} from '@angular/core';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-select-columns',
  templateUrl: './select-columns.component.html',
  styleUrls: ['./select-columns.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class SelectColumnsComponent implements OnInit {
  @Input()
  columns?: string[];

  constructor() {}

  ngOnInit(): void {}
}
