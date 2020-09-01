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
  indices: { [p: string]: any[] } = {};

  selectedDeviceType: string;
  selectedDevices: string[];
  selectedValueColumns: string[];

  constructor(
    private logService: LogsService,
    private router: Router,
    private routeStateService: RouteStateService
  ) {}

  ngOnInit(): void {
    this.routeStateService.pathParam.subscribe((pathParams) => {
      const deviceType = (pathParams.deviceType || '') as string;
      if (
        'deviceType' in Object.keys(pathParams) &&
        !(deviceType in Object.keys(this.indices))
      ) {
        this.router.navigateByUrl('/');
        return;
      }
      this.onSelectDeviceType(deviceType);
      this.selectedDevices = (pathParams.devices || []) as string[];
      this.selectedValueColumns = (pathParams.values || []) as string[];
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
  }

  onSelectDevices($event: string[]): void {
    this.selectedDevices = $event;
    this.navigate();
  }

  onSelectValueColumns($event: string[]): void {
    this.selectedValueColumns = $event;
    this.navigate();
  }

  navigate(): void {
    let uri = '/graph/';
    uri += this.selectedDeviceType + '/';
    if (!this.selectedDevices || this.selectedDevices.length <= 0) {
      uri += '-';
    } else {
      uri += this.selectedDevices;
    }
    uri += '/';
    if (!this.selectedValueColumns || this.selectedValueColumns.length <= 0) {
      uri += '-';
    } else {
      uri += this.selectedValueColumns;
    }
    uri = encodeURI(uri);
    this.router.navigateByUrl(uri).then();
  }
}
