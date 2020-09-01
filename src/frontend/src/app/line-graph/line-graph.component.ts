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
  values: string[];

  view = [0, 0];

  // options
  showXAxis = true;
  showYAxis = true;
  gradient = true;
  showLegend = true;
  showXAxisLabel = true;
  xAxisLabel = 'X Axis Label';
  showYAxisLabel = true;
  yAxisLabel = 'Y Axis Label';

  // line, area
  autoScale = true;

  /**
   * The data that is displayes as a line graph
   */
  data;

  constructor(
    private logsService: LogsService,
    private route: ActivatedRoute,
    private routeStateService: RouteStateService
  ) {
    console.log('constructor');
  }

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

      this.data = this.logsService.getValues(
        this.deviceType,
        this.devices,
        this.values
      );
    });
  }

  dateTickFormatting(val: any): string {
    if (val instanceof Date) {
      return (<Date>val).toLocaleString('de-DE');
    }
  }

  onSelect(event) {
    console.log(event);
  }
}
