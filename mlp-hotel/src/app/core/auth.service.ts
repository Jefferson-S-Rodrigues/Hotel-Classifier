import { Injectable } from '@angular/core';
import { Observable, throwError } from 'rxjs';
import { catchError, map } from 'rxjs/operators';
import {
  HttpClient,
  HttpHeaders,
  HttpErrorResponse,
  HttpParams,
} from '@angular/common/http';
import { Router } from '@angular/router';
import { User } from '../shared/models/user';
import { ApiConfigService } from './api-config.service';
@Injectable({
  providedIn: 'root',
})
export class AuthService extends ApiConfigService {
  headers = new HttpHeaders().set('Content-Type', 'application/json');
  currentUser = {};
  constructor(private http: HttpClient, public router: Router) { super(); }

  signIn(user: User) {
    const body = new HttpParams()
      .set('username', user.username)
      .set('password', user.password);
    return this.http.post<any>(`${this.apiUrl}/token`, body.toString(), {
        headers: new HttpHeaders()
          .set('Content-Type', 'application/x-www-form-urlencoded')
      })
      .subscribe({
        next: (res: any) => {
          localStorage.setItem('access_token', res.access_token);
          this.getUserProfile().subscribe((res) => {
            this.currentUser = res;
            this.router.navigate(['hotel']);
          });
        }
      });
  }

  getToken() {
    return localStorage.getItem('access_token');
  }

  get isLoggedIn(): boolean {
    let authToken = localStorage.getItem('access_token');
    return authToken !== null ? true : false;
  }

  doLogout() {
    let removeToken = localStorage.removeItem('access_token');
    if (removeToken == null) {
      this.router.navigate(['log-in']);
    }
  }

  getUserProfile(): Observable<any> {
    let api = `${this.apiUrl}/me`;
    return this.http.get(api, { headers: this.headers }).pipe(
      map((res) => {
        return res || {};
      }),
      catchError(this.handleError)
    );
  }

  newUserProfile(user: User): Observable<any> {
    let api = `${this.apiUrl}/new`;
    return this.http.post(api, user, { headers: this.headers });
  }

  handleError(error: HttpErrorResponse) {
    let msg = '';
    if (error.error instanceof ErrorEvent) {
      // client-side error
      msg = error.error.message;
    } else {
      // server-side error
      msg = `Error Code: ${error.status}\nMessage: ${error.message}`;
    }
    return throwError(msg);
  }
}