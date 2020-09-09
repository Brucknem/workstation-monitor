import { Component, Input, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { AddDialogComponent } from './add-dialog/add-dialog.component';

@Component({
  selector: 'app-add-button',
  templateUrl: './add-button.component.html',
  styleUrls: ['./add-button.component.css'],
})
export class AddButtonComponent implements OnInit {
  @Input()
  expanded: boolean;

  constructor(public dialog: MatDialog) {}

  ngOnInit(): void {}

  addNewCard(): void {
    this.dialog.open(AddDialogComponent);
  }
}
