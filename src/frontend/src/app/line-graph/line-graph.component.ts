import { Component, OnDestroy, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { map, takeUntil } from 'rxjs/operators';
import { Subject } from 'rxjs';
import { RouteStateService } from '../service/route-state.service';

@Component({
  selector: 'app-line-graph',
  templateUrl: './line-graph.component.html',
  styleUrls: ['./line-graph.component.css'],
})
export class LineGraphComponent implements OnInit {
  deviceType: string;
  devices: string[];
  values: string[];

  constructor(
    private route: ActivatedRoute,
    private routeStateService: RouteStateService
  ) {}

  ngOnInit(): void {
    this.route.paramMap.subscribe((params) => {
      const finalParams = { deviceType: params.get('deviceType') };
      let devices = params.get('devices').split(',');
      if (devices[0] === '-') {
        devices = [];
      }
      finalParams['devices'] = devices;
      let values = params.get('values').split(',');
      if (values[0] === '-') {
        values = [];
      }
      finalParams['values'] = values;
      this.routeStateService.updatePathParamState(finalParams);
    });
    this.routeStateService.pathParam.subscribe((pathParams) => {
      this.deviceType = pathParams['deviceType'] as string;
      this.devices = pathParams['devices'] as string[];
      this.values = pathParams['values'] as string[];
    });
  }
}
