import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export abstract class ApiConfigService {

  readonly apiUrl: string = `${environment.apiUrl}`;
}
