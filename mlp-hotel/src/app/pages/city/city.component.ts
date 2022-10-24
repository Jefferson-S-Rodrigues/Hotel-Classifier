import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { MatSnackBar } from '@angular/material/snack-bar';
import { HotelsService } from 'src/app/core/hotels.service';
import { HotelRequest } from 'src/app/shared/models/hotel-request';
import { Hotel } from 'src/app/shared/models/hotel';

@Component({
  selector: 'mlp-city',
  templateUrl: './city.component.html',
  styleUrls: ['./city.component.scss']
})
export class CityComponent implements OnInit {

  hotelForm: FormGroup = this.fb.group({
    name: '',
    index_name: 'hotel_name',
    n: 20,
    filter_name: ''
  });

  hotellist: Hotel[] = [];
  panelOpenState = true;

  constructor(
    public fb: FormBuilder,
    private hotelsService: HotelsService,
    private _snackBar: MatSnackBar,
  ) { }

  ngOnInit(): void {
    this.retornar();
  }
  retornar() {
    this.hotellist = [];
  }

  listHotel() {
    let hotel = this.hotelForm.getRawValue() as HotelRequest;
    this.hotelsService.getHotelList(hotel).subscribe({
      next: (result) => {
        this.retornar();
        for (let h of result) {
          this.hotellist.push({ "hotel": h } as Hotel);
        }
        this.panelOpenState = false;
        this.openSnackBar(`Foram encontrados ${this.hotellist.length} hotéis recomendados`, "Ok");
      },
      error: (err) => {
        this.openSnackBar(`${err.status} - ${err.error.detail}`, "Ok");
      },
    });
    this.hotelForm.reset;
    this.openSnackBar(`Buscando hotéis...`, "Fechar");
  }

  openSnackBar(message: string, action: string) {
    this._snackBar.open(message, action);
  }

  displayedColumns: string[] = ['position', 'hotel'];

}
