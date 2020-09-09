import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { TopBarComponent } from './top-bar/top-bar.component';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatAutocompleteModule } from '@angular/material/autocomplete';

import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatInputModule } from '@angular/material/input';
import { MatDividerModule } from '@angular/material/divider';
import { MatGridListModule } from '@angular/material/grid-list';

import { NgxFileHelpersModule } from 'ngx-file-helpers';
import { IndexSelectorComponent } from './index-selector/index-selector.component';
import { MatCardModule } from '@angular/material/card';
import { MatRadioModule } from '@angular/material/radio';
import { MatSelectModule } from '@angular/material/select';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { MatListModule } from '@angular/material/list';
import { SelectionListComponent } from './selection-list/selection-list.component';
import { IndexDropdownComponent } from './index-dropdown/index-dropdown.component';
import { MatExpansionModule } from '@angular/material/expansion';
import { LineGraphComponent } from './line-graph/line-graph.component';
import { BaseViewComponent } from './base-view/base-view.component';
import { NgxChartsModule } from '@swimlane/ngx-charts';
import { FlexLayoutModule } from '@angular/flex-layout';
import { AddDialogComponent } from './drawer/add-button/add-dialog/add-dialog.component';
import { MatDialogModule } from '@angular/material/dialog';
import { DrawerComponent } from './drawer/drawer.component';
import { LogsListComponent } from './drawer/logs-list/logs-list.component';
import { AddButtonComponent } from './drawer/add-button/add-button.component';
import { ErrorDialogComponent } from './drawer/logs-list/error-dialog/error-dialog.component';
import { MatTooltipModule } from '@angular/material/tooltip';
import { ContentComponent } from './content/content.component';
import { TableCardComponent } from './content/dashboard-cards/table-card/table-card.component';

@NgModule({
  declarations: [
    AppComponent,
    TopBarComponent,
    IndexSelectorComponent,
    SelectionListComponent,
    IndexDropdownComponent,
    LineGraphComponent,
    BaseViewComponent,
    AddDialogComponent,
    DrawerComponent,
    LogsListComponent,
    AddButtonComponent,
    ErrorDialogComponent,
    ContentComponent,
    TableCardComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatToolbarModule,
    MatIconModule,
    MatButtonModule,
    FontAwesomeModule,
    MatAutocompleteModule,
    FormsModule,
    MatInputModule,
    MatDividerModule,
    MatGridListModule,
    NgxFileHelpersModule,
    MatCardModule,
    MatRadioModule,
    MatSelectModule,
    ReactiveFormsModule,
    MatSidenavModule,
    MatCheckboxModule,
    MatListModule,
    MatExpansionModule,
    NgxChartsModule,
    FlexLayoutModule,
    MatDialogModule,
    MatTooltipModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
