import { Component, OnInit } from '@angular/core';
import { DashboardCardsService } from '../../../service/dashboard-cards.service';
import { Index, LogsService } from '../../../service/logs.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-add-dialog',
  templateUrl: './add-dialog.component.html',
  styleUrls: ['./add-dialog.component.css'],
})
export class AddDialogComponent implements OnInit {
  indices?: Observable<Index>;
  columns?: Observable<string[]>;

  ngOnInit(): void {}

  constructor(
    public logsService: LogsService,
    public dashboardCardsService: DashboardCardsService
  ) {}

  addCard(): void {
    this.dashboardCardsService.addCard('test');
  }

  selectLogFile(selectedLogFile: string): void {
    this.indices = this.logsService.getIndices(selectedLogFile);
    this.columns = this.logsService.getColumns(selectedLogFile);
  }
}
