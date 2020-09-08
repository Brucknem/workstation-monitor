import { Component, OnInit } from '@angular/core';
import { DashboardCardsService } from '../service/dashboard-cards.service';

@Component({
  selector: 'app-content',
  templateUrl: './content.component.html',
  styleUrls: ['./content.component.css'],
})
export class ContentComponent implements OnInit {
  constructor(public dashboardCardsService: DashboardCardsService) {}

  ngOnInit(): void {}
}
