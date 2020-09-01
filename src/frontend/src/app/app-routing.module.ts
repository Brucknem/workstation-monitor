import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LineGraphComponent } from './line-graph/line-graph.component';
import { BaseViewComponent } from './base-view/base-view.component';

const routes: Routes = [
  { path: 'graph/:deviceType/:devices/:values', component: LineGraphComponent },
  { path: '', component: BaseViewComponent, pathMatch: 'full' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
