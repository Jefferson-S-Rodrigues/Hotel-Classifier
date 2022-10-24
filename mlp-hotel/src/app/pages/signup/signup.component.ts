import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { MatSnackBar } from '@angular/material/snack-bar';
import { AuthService } from 'src/app/core/auth.service';
import { User } from 'src/app/shared/models/user';

@Component({
  selector: 'mlp-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.scss']
})
export class SignupComponent implements OnInit {

  signupForm: FormGroup;
  constructor(
    public fb: FormBuilder,
    public authService: AuthService,
    private _snackBar: MatSnackBar
  ) {
    this.signupForm = this.fb.group({
      username: [''],
      email: [''],
      password: [''],
      full_name: [''],
    });
  }
  ngOnInit(): void {

  }
  newUser() {
    let user = this.signupForm.getRawValue() as User;
    this.authService.newUserProfile(user).subscribe({
      next: (result) => {
        console.log(result);
        this.openSnackBar("Usuário criado com sucesso.", "OK");
        this.signupForm.reset();
      },
      error: (err) => {
        switch (err.status) {
          case 409: { this.openSnackBar(err.error.detail, "Corrija"); break; }
          default: { this.openSnackBar(`${err.status} - ${err.error.detail}`, "Corrija"); }
        }
      },
    });
  }

  openSnackBar(message: string, action: string) {
    this._snackBar.open(message, action);
  }

}
