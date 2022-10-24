export class User {
    _id!: string;
    username!: string;
    email!: string;
    password!: string;
    full_name!: string;
    disabled: boolean = false;
    create_at!: Date;
}