import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HotelRequest } from '../shared/models/hotel-request';
import { ApiConfigService } from './api-config.service';

@Injectable({
  providedIn: 'root'
})
export class HotelsService extends ApiConfigService {
  headers = new HttpHeaders().set('Content-Type', 'application/json');

  constructor(private http: HttpClient) { super(); }

  getHotelList(hotel: HotelRequest): Observable<any> {
    return this.http.post(`${this.apiUrl}/hotellist`, hotel, {headers: this.headers});
  }
}
