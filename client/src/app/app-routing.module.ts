import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { OmokComponent } from './omok/omok.component';
import { ManagerComponent } from './manager/manager.component';

const routes: Routes = [
  { path: 'index', component: OmokComponent },
  { path: 'room/:id', component: OmokComponent },
  { path: 'manager', component: ManagerComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
