import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';
import { ParamMap } from '@angular/router';

@Injectable({
  providedIn: 'root',
})
export class RouteStateService {
  private pathParamState = new BehaviorSubject<{
    [key: string]: string | string[];
  }>({});

  pathParam: Observable<{ [key: string]: string | string[] }>;

  constructor() {
    this.pathParam = this.pathParamState.asObservable();
  }

  updatePathParamState(newPathParam: {
    [key: string]: string | string[];
  }): void {
    this.pathParamState.next(newPathParam);
  }
}
