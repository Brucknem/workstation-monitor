import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { v4 } from 'uuid';

export interface IDashboardCard {
  uuid: string;
  name: string;
}

@Injectable({
  providedIn: 'root',
})
export class DashboardCardsService {
  private cards: IDashboardCard[] = [];

  public getCards(): Observable<IDashboardCard[]> {
    return of(this.cards);
  }

  addCard(name: string): void {
    const uuid = v4();

    this.cards.push({ name, uuid });
  }

  deleteCard(uuid: string): void {
    const index = this.cards.findIndex((card) => card.uuid === uuid);
    if (index >= 0 && index < this.cards.length) {
      this.cards.splice(index, 1);
    }
  }
}
