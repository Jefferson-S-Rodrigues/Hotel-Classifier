import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { AuthService } from 'src/app/core/auth.service';

@Component({
  selector: 'mlp-signin',
  templateUrl: './signin.component.html',
  styleUrls: ['./signin.component.scss']
})
export class SigninComponent {

  signinForm: FormGroup;
  constructor(
    public fb: FormBuilder,
    public authService: AuthService
  ) {
    this.signinForm = this.fb.group({
      username: [''],
      password: [''],
    });
  }
  loginUser() {
    this.authService.signIn(this.signinForm.value);
  }
}
