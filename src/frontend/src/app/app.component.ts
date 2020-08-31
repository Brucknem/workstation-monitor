import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  title = 'frontend';
  showFiller = false;

  componentAdded($event: any) {
    console.log($event);
  }

  componentRemoved($event: any) {
    console.log($event);
  }
}
