import { Component, OnInit, ViewChild } from '@angular/core';
import { FilePickerDirective, ReadFile, ReadMode } from 'ngx-file-helpers';

@Component({
  selector: 'app-top-bar',
  templateUrl: './top-bar.component.html',
  styleUrls: ['./top-bar.component.css'],
})
export class TopBarComponent implements OnInit {
  public readMode = ReadMode.dataURL;
  public picked: ReadFile;
  public status: string;

  constructor() {}

  @ViewChild('myFilePicker')
  private filePicker: FilePickerDirective;

  onReadStart(fileCount: number) {
    this.status = `Reading ${fileCount} file(s)...`;
  }

  onFilePicked(file: ReadFile) {
    this.picked = file;
    console.log(this.picked);
  }

  onReadEnd(fileCount: number) {
    this.status = `Read ${fileCount} file(s) on ${new Date().toLocaleTimeString()}.`;
    this.filePicker.reset();
  }

  ngOnInit(): void {}
}
