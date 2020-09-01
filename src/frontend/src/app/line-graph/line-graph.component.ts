import { Component, OnDestroy, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { RouteStateService } from '../service/route-state.service';
import { LogsService } from '../service/logs.service';

@Component({
  selector: 'app-line-graph',
  templateUrl: './line-graph.component.html',
  styleUrls: ['./line-graph.component.css'],
})
export class LineGraphComponent implements OnInit {
  deviceType: string;
  devices: string[];
  values: string;

  multi = {};
  view: any[] = [700, 400];

  // options
  showXAxis = true;
  showYAxis = true;
  gradient = true;
  showLegend = true;
  showXAxisLabel = true;
  xAxisLabel = 'Country';
  showYAxisLabel = true;
  yAxisLabel = 'Population';

  colorScheme = {
    domain: ['#5AA454', '#A10A28', '#C7B42C', '#AAAAAA'],
  };

  // line, area
  autoScale = true;

  result;

  constructor(
    private logsService: LogsService,
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
      let value = params.get('values');
      if (value === '-') {
        value = '';
      }
      finalParams['value'] = value;
      this.routeStateService.updatePathParamState(finalParams);
    });
    this.routeStateService.pathParam.subscribe((pathParams) => {
      this.deviceType = pathParams['deviceType'] as string;
      this.devices = pathParams['devices'] as string[];
      this.values = pathParams['value'] as string;
    });
    this.result = this.logsService.getValues(
      this.deviceType,
      this.devices,
      this.values
    );
  }

  onSelect(event) {
    console.log(event);
  }
}
