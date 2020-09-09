import { Component, OnInit } from '@angular/core';
import { MatDialogRef } from '@angular/material/dialog';
import { DashboardCardsService } from '../../../service/dashboard-cards.service';

@Component({
  selector: 'app-add-dialog',
  templateUrl: './add-dialog.component.html',
  styleUrls: ['./add-dialog.component.css'],
})
export class AddDialogComponent implements OnInit {
  constructor(
    public dialogRef: MatDialogRef<AddDialogComponent>,
    public dashboardCardsService: DashboardCardsService
  ) {}

  ngOnInit(): void {}

  addCard($event: MouseEvent): void {
    console.log($event);
    this.dashboardCardsService.addCard('test');
    this.dialogRef.close();
  }
}
