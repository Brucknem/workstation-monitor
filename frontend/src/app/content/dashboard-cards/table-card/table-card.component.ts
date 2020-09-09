import { Component, Input, OnInit } from '@angular/core';
import {
  DashboardCardsService,
  IDashboardCard,
} from '../../../service/dashboard-cards.service';

@Component({
  selector: 'app-table-card',
  templateUrl: './table-card.component.html',
  styleUrls: ['./table-card.component.css'],
})
export class TableCardComponent implements OnInit {
  @Input()
  card: IDashboardCard;

  constructor(public dashboardCardsService: DashboardCardsService) {}

  ngOnInit(): void {}
}
