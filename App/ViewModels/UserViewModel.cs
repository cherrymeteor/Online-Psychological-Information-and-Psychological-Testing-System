﻿using System;
using System.Collections.ObjectModel;
using System.Net.Http;
using System.Threading.Tasks;
using App.Helpers;
using App.Models;
using App.Services;
using GalaSoft.MvvmLight;
using Windows.UI.Xaml;

namespace App.ViewModels
{
    public class UserViewModel : ViewModelBase
    {
        public OrangeService OrangeService => OrangeService.Current;

        public UserViewModel()
        {
            ViewModelConnHelper.OnMessageTransmitted += OnMessageTransmitted;
            Task x = LoadAsync();
        }

        public async Task LoadAsync(bool initialize = true)
        {
            Loading = Visibility.Visible;
            if (initialize)
            {
                await Task.Delay(800);
            }
            else
            {
                await Task.Delay(2000);
            }

            if (initialize || Next != null)
            {
                var request = Next == null ?
                new HttpRequestMessage(HttpMethod.Get, "/api/posts-favor/") :
                new HttpRequestMessage(HttpMethod.Get, Next);

                var result = await OrangeService.Current.SendRequestAsync<Pagination<PostFavor>>(request);
                if (result.Success)
                {
                    var data = result.Data;
                    Next = data?.next;
                    foreach (var item in data?.results)
                    {
                        Items.Add(item);
                    }
                }
            }

            Loading = Visibility.Collapsed;
        }

        private void OnMessageTransmitted(string message)
        {
            if (message == "avatar_update")
                RaisePropertyChanged("OrangeService");
        }

        private Visibility _loading = Visibility.Collapsed;
        public Visibility Loading { get => _loading; set => Set(ref (_loading), value); }

        private Uri _next = null;

        public Uri Next
        {
            get { return _next; }

            set { Set(ref _next, value); }
        }

        public ObservableCollection<PostFavor> _items = new ObservableCollection<PostFavor>();

        public ObservableCollection<PostFavor> Items
        {
            get { return _items; }
            set { Set(ref _items, value); }
        }
    }
}

