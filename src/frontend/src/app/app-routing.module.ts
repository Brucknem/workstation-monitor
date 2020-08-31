import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LineGraphComponent } from './line-graph/line-graph.component';
import { BaseViewComponent } from './base-view/base-view.component';

const routes: Routes = [
  { path: '', component: BaseViewComponent, pathMatch: 'full' },
  { path: 'graph/:deviceType/:devices/:values', component: LineGraphComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
