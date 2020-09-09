import { Component, Input, OnInit } from '@angular/core';
import { LogsService } from '../../service/logs.service';
import { MatDialog } from '@angular/material/dialog';
import { ErrorDialogComponent } from './error-dialog/error-dialog.component';

@Component({
  selector: 'app-logs-list',
  templateUrl: './logs-list.component.html',
  styleUrls: ['./logs-list.component.css'],
})
export class LogsListComponent implements OnInit {
  @Input()
  expanded: boolean;

  constructor(public logsService: LogsService, public dialog: MatDialog) {}

  ngOnInit(): void {}

  public deleteLog(name: string): void {
    this.logsService.deleteLog(name);
  }

  onFileChanged($event: Event): void {
    const selectedFile = ($event.target as HTMLInputElement).files[0];
    const name = selectedFile.name;

    const fileReader = new FileReader();
    fileReader.onload = () => {
      try {
        if (typeof fileReader.result === 'string') {
          this.logsService.addLog(
            name.split('.json')[0],
            JSON.parse(fileReader.result)
          );
        }
      } catch (e) {
        this.openErrorDialog(e);
      }
    };
    fileReader.onerror = (error) => {
      this.openErrorDialog(error);
    };
    fileReader.readAsText(selectedFile, 'UTF-8');
  }

  private openErrorDialog(error: any): void {
    this.dialog.open(ErrorDialogComponent, {
      data: { error },
    });
  }
}
