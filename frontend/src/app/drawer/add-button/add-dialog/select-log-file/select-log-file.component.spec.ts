import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SelectLogFileComponent } from './select-log-file.component';

describe('SelectLogFileComponent', () => {
  let component: SelectLogFileComponent;
  let fixture: ComponentFixture<SelectLogFileComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SelectLogFileComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SelectLogFileComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
