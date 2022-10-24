import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from './core/auth.service';

@Component({
  selector: 'mlp-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  constructor(public authService: AuthService, public router: Router) { }
  logout() {
    this.authService.doLogout();
    this.router.navigate(['user-profile/']);
  }
  title = 'Hotel Recomender';
}
