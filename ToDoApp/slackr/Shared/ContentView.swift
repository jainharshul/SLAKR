//
//  ContentView.swift
//  Shared
//
//  Created by Harshul Jain on 1/21/22.
//  Mike Jiang, joined 1/21/21. 

import SwiftUI
import UserNotifications


struct ContentView: View {
    @State var task: String = ""
    @State var taskArray: [ItemModel] = [] {
        didSet{
            saveItems()
        }
    }
    
    init(){
        getItems()
    }
    
    let itemsKey: String = "items_list"

    
    var body: some View {
        
        ZStack{
            Image("background3")
                .resizable()
                .aspectRatio(contentMode: /*@START_MENU_TOKEN@*/.fill/*@END_MENU_TOKEN@*/)
                .ignoresSafeArea()
            List{
                ForEach(taskArray) {item in
                    ListRowView(item: item)
                }.onDelete(perform: deleteItem)
            }
            .frame(width: 400.0, height: CGFloat(changeSize()))
            .offset(x: 0, y: 0)
            
            
            VStack{
                Text("ToDo List:")
                    .font(.largeTitle)
                    .fontWeight(.ultraLight)
                    .foregroundColor(Color.black)
                
                HStack{
                        
                    Spacer()
                    
                    TextField("List another task here...", text: $task)
                        .textFieldStyle(RoundedBorderTextFieldStyle())
                        .padding(.horizontal, 26.0)
                    
                    Spacer()
                    
                    Button(action: {
                        saveTask(task: task)
                        task = ""
                        
                            
                    }, label: {
                        Text("Add")
                            .font(.title3)
                            .fontWeight(.ultraLight)
                            .foregroundColor(Color.black)
                            .padding()
                            .frame(width: 100.0, height: 35.0)
                            .background(Color.gray.opacity(0.3).cornerRadius(35))
                    })
                    .padding(.trailing, 35.0)
                }
                
                
                
               
                Spacer()
                
                Button(action: {
                    clearAll()
                }, label: {
                    Text("Clear")
                        .font(.title3)
                        .fontWeight(.ultraLight)
                        .foregroundColor(Color.black)
                        .padding()
                        .frame(width: 100.0, height: 35.0)
                        .background(Color.gray.opacity(0.4).cornerRadius(35))

                })
                .padding(.trailing, 35.0)
                
                Button(action: {
                    print("startworking button clicked")
                }, label: {
                    Image("startworking")
                })
                
               
            }
        }
       
    }
    
    func deleteItem(indexSet: IndexSet){
        taskArray.remove(atOffsets: indexSet)
    }
    
    func saveTask(task: String){
        if (task.count >= 1){
            taskArray.append(ItemModel(title: task))
        }
    }
    
    func clearAll(){
        taskArray.removeAll()
    }
    
    func changeSize() -> Double{
        let size = (taskArray.count) * 50
        if (size <= 500){
            return Double(size)
        }
        else{
            return 500
        }
        
    }
    
    func saveItems(){
        if let encodedData = try? JSONEncoder().encode(taskArray){
            UserDefaults.standard.setValue(encodedData, forKey: itemsKey)
            
        }
    }
    
    func getItems(){
        guard
            let data = UserDefaults.standard.data(forKey: itemsKey),
            let savedItems = try? JSONDecoder().decode([ItemModel].self, from: data)
        else {return}
        self.taskArray = savedItems
    
    }
}


struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}


