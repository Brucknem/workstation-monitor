import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { map, tap } from 'rxjs/operators';

export interface IDashboardCard {
  name: string;
}

@Injectable({
  providedIn: 'root',
})
export class DashboardCardsService {
  private cards: IDashboardCard[] = [];

  constructor() {
    for (let i = 0; i < 5; i++) {
      this.addCard('test-card: ' + i);
    }
  }

  public getCards(): Observable<IDashboardCard[]> {
    return of(this.cards);
  }

  addCard(name: string): void {
    this.cards.push({ name });
  }
}
