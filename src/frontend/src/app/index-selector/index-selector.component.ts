import { Component, OnInit } from '@angular/core';
import { LogsService } from '../service/logs.service';
import { Router } from '@angular/router';
import { RouteStateService } from '../service/route-state.service';

@Component({
  selector: 'app-index-selector',
  templateUrl: './index-selector.component.html',
  styleUrls: ['./index-selector.component.css'],
})
export class IndexSelectorComponent implements OnInit {
  log: object;
  columns: string[];
  valueColumns: string[];
  indices: { [p: string]: any[] };

  selectedDeviceType: string;
  selectedDevices: string[];
  selectedValueColumn: string;

  constructor(
    private logService: LogsService,
    private router: Router,
    private routeStateService: RouteStateService
  ) {}

  ngOnInit(): void {
    this.routeStateService.pathParam.subscribe((pathParams) => {
      if (!('deviceType' in pathParams)) {
        return;
      }
      this.onSelectDeviceType(pathParams['deviceType'] as string);
      this.selectedDevices = pathParams['devices'] as string[];
      this.selectedValueColumn = pathParams['value'] as string;
    });
    this.getLogs();
    this.getColumns();
    this.getIndices();
  }

  getLogs(): void {
    this.logService.getLogs().subscribe((log) => (this.log = log));
  }

  getColumns(): void {
    this.logService
      .getColumns()
      .subscribe((columns) => (this.columns = columns));
  }

  getIndices(): void {
    this.logService
      .getIndices()
      .subscribe((indices) => (this.indices = indices));
  }

  onSelectDeviceType($event: string): void {
    this.selectedDeviceType = $event;
    this.valueColumns = Object.assign([], this.columns);
    const index = this.valueColumns.indexOf(this.selectedDeviceType, 0);
    if (index > -1) {
      this.valueColumns.splice(index, 1);
    }
    console.log(this.selectedDeviceType);
  }

  onSelectDevices($event: string[]): void {
    this.selectedDevices = $event;
    this.navigate();
  }

  onSelectValueColumns($event: string): void {
    this.selectedValueColumn = $event;
    this.navigate();
  }

  navigate(): void {
    let uri = '/graph/';
    uri += this.selectedDeviceType + '/';
    if (this.selectedDevices.length <= 0) {
      uri += '-';
    } else {
      uri += this.selectedDevices;
    }
    uri += '/';
    if (!this.selectedValueColumn) {
      uri += '-';
    } else {
      uri += this.selectedValueColumn;
    }
    uri = encodeURI(uri);
    this.router.navigateByUrl(uri).then();
  }
}
