/*
  Project Prodtools
  Test driver module

  module for csv testing

  ToraNova 2019
  chia_jason96@live.com
*/
#include "testlist.hpp"

#include <prodtools/csv/reader.hpp>
#include <prodtools/csv/writer.hpp>
using namespace std;

void csv_test0(){
  csvreader::libtest();


  csvreader::DoubleReader cr = csvreader::DoubleReader();
  uint16_t t = cr.readcsv("assets/double.csv");
  cout << "File read results : " << t << endl;
  cout << "CSV size row:" << cr.getRowCount() << " col:"<< cr.getColCount() << endl;

  csvwriter::writecsv_double("cxx_test_output.csv",cr.borrow_mdouble(),cr.getRowCount(),cr.getColCount(),';');

  return;

}
