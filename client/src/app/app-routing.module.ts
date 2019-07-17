import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { OmokComponent } from './omok/omok.component';

const routes: Routes = [
  { path: 'index', component: OmokComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
